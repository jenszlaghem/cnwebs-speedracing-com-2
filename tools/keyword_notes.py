from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime


@dataclass
class Tag:
    """Represents a single tag attached to a note."""
    name: str
    category: str = "general"


@dataclass
class KeywordNote:
    """A structured note associated with a keyword and source URL."""
    keyword: str
    title: str
    content: str
    source_url: str
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[Tag] = field(default_factory=list)
    importance: int = 5  # 1–10

    def add_tag(self, tag_name: str, tag_category: str = "general") -> None:
        """Add a tag to this note."""
        self.tags.append(Tag(name=tag_name, category=tag_category))

    def summary(self) -> str:
        """Return a one-line summary of the note."""
        tag_names = ", ".join(t.name for t in self.tags) if self.tags else "no tags"
        return f"[{self.keyword}] {self.title[:40]}... | tags: {tag_names}"


def format_note_detailed(note: KeywordNote) -> str:
    """Return a detailed formatted string of a KeywordNote."""
    lines = []
    lines.append(f"Keyword: {note.keyword}")
    lines.append(f"Title: {note.title}")
    lines.append(f"Content: {note.content}")
    lines.append(f"Source: {note.source_url}")
    lines.append(f"Created: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    if note.tags:
        tags_str = "; ".join(f"{t.name} ({t.category})" for t in note.tags)
        lines.append(f"Tags: {tags_str}")
    else:
        lines.append("Tags: (none)")
    lines.append(f"Importance: {note.importance}/10")
    lines.append("-" * 40)
    return "\n".join(lines)


def format_note_brief(note: KeywordNote) -> str:
    """Return a brief single-line representation of a note."""
    return f"{note.keyword} | {note.title} | {note.source_url}"


def generate_sample_notes() -> List[KeywordNote]:
    """Create a list of sample KeywordNote instances with demo data."""
    note1 = KeywordNote(
        keyword="极速赛车",
        title="极速赛车最新赛事速报",
        content="极速赛车锦标赛本周末在全新赛道举行，多位顶尖车手参与角逐，现场气氛热烈。",
        source_url="https://cnwebs-speedracing.com/news/latest",
        importance=8,
    )
    note1.add_tag("赛事", "category")
    note1.add_tag("极速赛车", "keyword")

    note2 = KeywordNote(
        keyword="极速赛车",
        title="极速赛车改装技术解析",
        content="深度分析极速赛车的引擎优化、悬挂调校和空气动力学套件选择。",
        source_url="https://cnwebs-speedracing.com/tech/tuning",
        importance=6,
    )
    note2.add_tag("改装", "category")
    note2.add_tag("技术", "category")

    note3 = KeywordNote(
        keyword="极速赛车",
        title="极速赛车历史回顾",
        content="从诞生到如今，极速赛车如何成为全球瞩目的竞速品牌。",
        source_url="https://cnwebs-speedracing.com/history",
        importance=5,
    )
    note3.add_tag("历史", "category")
    note3.add_tag("回顾", "general")

    return [note1, note2, note3]


def search_notes_by_keyword(notes: List[KeywordNote], keyword: str) -> List[KeywordNote]:
    """Return notes whose keyword field matches the given string (case‑insensitive)."""
    return [n for n in notes if n.keyword.lower() == keyword.lower()]


def print_all_notes(notes: List[KeywordNote], detailed: bool = False) -> None:
    """Print every note in the list, in either detailed or brief format."""
    for i, note in enumerate(notes, start=1):
        print(f"Note #{i}")
        if detailed:
            print(format_note_detailed(note))
        else:
            print(format_note_brief(note))


# -------------------------------------------------------------------
# Example usage when script is run directly
if __name__ == "__main__":
    samples = generate_sample_notes()
    print("=== All sample notes (brief) ===")
    print_all_notes(samples, detailed=False)

    print("\n=== Search notes for '极速赛车' ===")
    found = search_notes_by_keyword(samples, "极速赛车")
    print(f"Found {len(found)} note(s):")
    for n in found:
        print(format_note_brief(n))

    print("\n=== Detailed view of first note ===")
    if samples:
        print(format_note_detailed(samples[0]))