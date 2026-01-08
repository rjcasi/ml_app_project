from fastapi import APIRouter
import matplotlib.pyplot as plt
import base64
from io import BytesIO

router = APIRouter(prefix="/visualization", tags=["Visualization"])

@router.get("/ping")
def ping():
    return {"message": "Visualization router is alive"}

def fig_to_base64(fig):
    buf = BytesIO()
    fig.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

@router.post("/line")
def line_chart(x: list[int], y: list[int]):
    fig, ax = plt.subplots()
    ax.plot(x, y)
    image_b64 = fig_to_base64(fig)
    return {"chart": "line", "image_base64": image_b64}

@router.post("/bar")
def bar_chart(categories: list[str], values: list[int]):
    fig, ax = plt.subplots()
    ax.bar(categories, values)
    image_b64 = fig_to_base64(fig)
    return {"chart": "bar", "image_base64": image_b64}

@router.post("/pie")
def pie_chart(labels: list[str], sizes: list[int]):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%")
    image_b64 = fig_to_base64(fig)
    return {"chart": "pie", "image_base64": image_b64}