import streamlit as st
import json
import urllib.request

st.set_page_config(page_title="FocusTask CLI & Web", page_icon="🎯")
st.title("🎯 FocusTask CLI - Gestão de Produtividade")

if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"id": 1, "title": "Estudar para o Bootcamp II", "done": False},
        {"id": 2, "title": "Criar a Issue no GitHub", "done": True}
    ]

def fetch_motivational_advice():
    try:
        url = "https://api.adviceslip.com/advice"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode())
            return data["slip"]["advice"]
    except Exception:
        return "Mantenha o foco e continue progredindo em suas metas!"

st.subheader("Nova Tarefa")
new_task = st.text_input("O que você precisa fazer hoje?", placeholder="Ex: Escrever testes de integração...")

if st.button("Adicionar Tarefa"):
    if new_task.strip():
        new_id = max([t["id"] for t in st.session_state.tasks], default=0) + 1
        st.session_state.tasks.append({"id": new_id, "title": new_task.strip(), "done": False})
        st.success("Tarefa adicionada com sucesso!")
        st.rerun()

st.subheader("Suas Atividades")
for task in st.session_state.tasks:
    col1, col2 = st.columns([0.8, 0.2])
    if task["done"]:
        col1.write(f"~~{task['title']}~~ ✅ (Concluída)")
    else:
        col1.write(f"⬜ {task['title']}")
        if col2.button("Concluir", key=f"done_{task['id']}"):
            task["done"] = True
            advice = fetch_motivational_advice()
            st.session_state.latest_advice = advice
            st.rerun()

if "latest_advice" in st.session_state:
    st.info(f"💡 **Conselho de Foco do Dia:** {st.session_state.latest_advice}")
