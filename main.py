import json
import jwt
import os
import flask
import hashlib
from dotenv import load_dotenv
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

app = flask.Flask(__name__)
load_dotenv()


@app.route('/<lang>/<file_format>/<save>/<jwt_token>', methods=['GET'])
def get(lang, file_format, save, jwt_token):
    """Endpoint по которому идет обращение через метод GET."""
    data = parse_data_json(lang)
    jwt_hash = hashlib.md5(jwt_token.encode()).hexdigest()
    jwt_token = parse_jwt_json(jwt_token)
    file_path = get_file_path(file_format, jwt_hash)

    if not os.path.isfile(file_path):
        render(
            data,
            jwt_token,
            file_path
        )

    return flask.send_file(file_path, as_attachment=(save == 'true'))


def get_file_path(file_format, jwt_hash):
    return "temp/certificate-{}.{}".format(jwt_hash, file_format)


def parse_data_json(lang):
    """Получение json данных из заранее сконфигурированных файлов."""
    with open("res/{}.json".format(lang)) as json_file:
        return json.load(json_file)


def parse_jwt_json(data):
    """Получение и валидирование JWT входящего токена."""
    return jwt.decode(data, os.getenv("JWT_KEY"), algorithms=[os.getenv("JWT_ALGORITHM")])


def render(data_json, jwt_token, file_name):
    """Генерация изображения на основе входных данных."""
    img = Image.open(data_json["config"]["bg_path"])
    draw = ImageDraw.Draw(img)

    for key in data_json:
        if key == "config" :
            continue

        value = data_json[key]

        if "dependence" in value:
            if not is_dependence(data_json, jwt_token, value["dependence"]):
                continue

        if key not in jwt_token and "text" not in value:
            continue
        else:
            text = value["text"] if "text" in value else jwt_token[key]

        font = ImageFont.truetype(
            data_json["config"]["font"][str(value["weight"])],
            value["text_size"]
        )

        draw.text(
            (value["x"], value["y"]),
            text,
            value["text_color"],
            font=font
        )

    if file_name.find(".pdf") != -1:
        img = img.convert('RGB')

    img.save(file_name)


def is_dependence(data_json, jwt_token, dependence_key):
    """Проверка зависимости. Если у зависимости имеется text, будет возвращен True."""
    if dependence_key in data_json:
        if "text" in data_json:
            return False

    if dependence_key in jwt_token:
        return True

    return False


app.run(host=os.getenv("HOST"), port=os.getenv("PORT"))
