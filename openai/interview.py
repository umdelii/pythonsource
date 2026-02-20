from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import gradio as gr


load_dotenv(find_dotenv())

client = OpenAI()


# 장르를 받은 후 작가에게 알맞는 질문 8개 추출
# 장르 특징 5줄 정리
def interview_text(text):

    if not text.strip():
        return gr.Error("장르를 올바르게 입력하십시오")

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "developer",
                "content": "당신은 20년차 프로인터뷰어. 여지껏 인터뷰 진행했던 사람만 1.5만명. 특히 책에 흥미가 많고 독서가 취미. 작가 인터뷰에 강점이 있음",
            },
            {
                "role": "user",
                "content": f"""
                다음 장르의 특징을 분석하고, 그 분석을 바탕으로 인터뷰 질문을 작성하세요

                [장르]
                {text}

                요구사항
                1. 장르 특징 5줄로 정리하기
                2. 인터뷰 질문 최소 8개 이상 작성하기
                """,
            },
        ],
    )

    return response.output_text


demo = gr.Interface(
    fn=interview_text,
    inputs=[
        gr.Text(label="장르", placeholder="장르"),
    ],
    outputs=gr.Markdown(),
    title="📚작가 인터뷰 질문 생성 프로그램 구현",
)

demo.launch()
