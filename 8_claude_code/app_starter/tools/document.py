from markitdown import MarkItDown, StreamInfo
from io import BytesIO
from pathlib import Path
from pydantic import Field


def binary_document_to_markdown(binary_data: bytes, file_type: str) -> str:
    """Converts binary document data to markdown-formatted text."""
    md = MarkItDown()
    file_obj = BytesIO(binary_data)
    stream_info = StreamInfo(extension=file_type)
    result = md.convert(file_obj, stream_info=stream_info)
    return result.text_content


def document_path_to_markdown(
    path: str = Field(description="Path to a PDF or DOCX file to convert"),
) -> str:
    """Convert a PDF or DOCX file to markdown-formatted text.

    Reads a document file from the given path and converts its contents
    to markdown format using the MarkItDown library.

    When to use:
    - When you need to extract text content from PDF or DOCX files
    - When you want document content in a portable markdown format

    When NOT to use:
    - For non-document files (images, spreadsheets, etc.)
    - When you need to preserve exact document formatting

    Examples:
        >>> document_path_to_markdown("/path/to/document.pdf")
        "# Document Title\\n\\nDocument content..."
        >>> document_path_to_markdown("/path/to/report.docx")
        "# Report\\n\\nReport content..."
    """
    file_path = Path(path)
    binary_data = file_path.read_bytes()
    file_type = file_path.suffix
    return binary_document_to_markdown(binary_data, file_type)
