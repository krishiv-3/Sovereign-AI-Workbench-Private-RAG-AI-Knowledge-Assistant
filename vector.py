from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

import os
import glob
from pypdf import PdfReader


# ==============================
# 1. PDF DATA LOCATION
# ==============================

data_folder = "./CGC_FINAL_DATA"

db_location = "./cgc_chroma_db"


# ==============================
# 2. EMBEDDING MODEL
# ==============================

embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)


# ==============================
# 3. TEXT SPLITTER
# ==============================

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)


# ==============================
# 4. LOAD PDF DOCUMENTS
# ==============================

documents = []

pdf_files = glob.glob(
    os.path.join(data_folder, "**", "*.pdf"),
    recursive=True
)

print(f"Found {len(pdf_files)} PDF files.")


for pdf_path in pdf_files:

    print(f"Reading: {pdf_path}")

    reader = PdfReader(pdf_path)

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            chunks = text_splitter.split_text(text)

            for chunk in chunks:

                document = Document(
                    page_content=chunk,
                    metadata={
                        "source": pdf_path,
                        "page": page_number + 1
                    }
                )

                documents.append(document)


print(f"Created {len(documents)} document chunks.")


# ==============================
# 5. CREATE VECTOR DATABASE
# ==============================

vector_store = Chroma(
    collection_name="cgc_documents",
    persist_directory=db_location,
    embedding_function=embeddings
)


# ==============================
# 6. ADD DOCUMENTS
# ==============================

existing_count = vector_store._collection.count()

print(f"Documents currently in ChromaDB: {existing_count}")

if existing_count == 0:

    print("Adding documents to vector database...")

    vector_store.add_documents(
        documents=documents
    )

    print("Vector database created successfully!")

else:

    print(f"Vector database already contains {existing_count} documents.")

# ==============================
# 7. RETRIEVER
# ==============================

retriever = vector_store.as_retriever(
    search_kwargs={
        "k": 8
    }
)