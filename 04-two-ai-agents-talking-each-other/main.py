import asyncio

from autogen_core import AgentId, SingleThreadedAgentRuntime
from autogen_core.models import SystemMessage

from assistant import Assistant
from client import get_model_client
from class_types import (Message, AgentProfile)

async def main() -> None:
    runtime = SingleThreadedAgentRuntime()

    agent_one = await Assistant.register(
        runtime,
        "isis",
        lambda: Assistant(
            name="🤖 Isis",
            model_client=get_model_client("dolphin3"),
            system_messages=[
                SystemMessage(
                    content="Tu nombre es Isis, eres la CTO de una importante empresa de tecnología y vas hacer una entrevista para el cargo de Frontend Engineer"
                    "Vas a hacer preguntas de tipo quiz en Frontend para medir sus conocimientos."
                    "En caso de que consideres que la persona que entrevista, no responde correctamente. Dile que has acabado la entrevista y que luego le daras feedback. Vas a hacer las preguntas más dificiles que se te ocurran ya que el cargo es muy importante."
                    "Si consideras que el candidato es el correcto despues de 5 preguntas, puedes preguntarle sobre sus aspiraciones salariales y si tiene alguna pregunta para ti."
                    "Por favor manten una actitud profesional durante la entrevista y conversación."
                )
            ]
        ),
    )

    agent_two = await Assistant.register(
        runtime,
        "nala",
        lambda: Assistant(
            name="🦄 Nala",
            model_client=get_model_client("dolphin3"),
            system_messages=[
                SystemMessage(
                    content="Tu nombre es Nala, estas en una entrevista de trabajo y tienes experiencia como Junior Developer."
                    "Si te llegan a preguntar sobre tu aspiración salarial, trata de mantener un rango por encima de 100,000 CAD al año y negocia muy bien."
                )
            ]
        ),
    )

    runtime.start()
    await runtime.send_message(
        Message("Muy bien, empecemos, esta es una entrevista para el cargo de Tech Lead. ¿Como te llamas y cual es tu background?"),
        sender=AgentId(agent_one, "default"),
        recipient=AgentId(agent_two, "default"),
    )
    await runtime.stop_when_idle()

asyncio.run(main())