from yandex_chain import YandexEmbeddings
from langchain_community.vectorstores import FAISS
from yandex_chain import YandexLLM
from langchain.chains import RetrievalQA

api_key = "***"
folder_id = "***"

embeddings = YandexEmbeddings(api_key=api_key, folder_id=folder_id)
vectorstore = FAISS.load_local(folder_path='data/ai_programs', embeddings=embeddings,
                               allow_dangerous_deserialization=True)

instruction_text = (
    'Ты интеллектуальный помощник, который помогает абитуриентам выбрать одну из двух программ магистратуры: Искусственный Интеллект (AI)'
    ' или Управление ИИ Продуктами (AI Product Management). Получай информацию о программах из файлов. Отвечай на вопросы пользователя по поводу'
    ' выбора образовательных программ. Игнорируй вопросы не связанные с обучением в магистратуре.')

llm = YandexLLM(api_key=api_key, folder_id=folder_id, instruction_text=instruction_text)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
    return_source_documents=True
)


def answer_question(question: str) -> str:
    """
    Обрабатывает вопрос через QA-цепочку на базе YandexGPT и возвращает ответ.
    """
    # Пример:
    result = qa_chain.invoke({"query": question})
    return result["result"]
