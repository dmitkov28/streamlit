import httpx
import streamlit
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def build_url(subreddit: str, post_type: str) -> str:
    if post_type not in ["hot", "top", "new", "rising"]:
        raise ValueError("Invalid post type")
    url = f"https://reddit.com/{process_subreddit_name(subreddit)}/{post_type}.json"
    return url


def process_subreddit_name(subreddit_name: str) -> str:
    if subreddit_name.startswith("r/"):
        return subreddit_name
    else:
        return f"r/{subreddit_name}"


def get_posts(subreddit: str, post_type: str) -> list:
    url = build_url(subreddit=subreddit, post_type=post_type)

    data = httpx.get(url=url, follow_redirects=True).json()

    # gets rid of unnecessary fields coming from the reddit api
    try:
        posts = [item.get("data", {}) for item in data.get("data", {}).get("children")]
        return posts
    except Exception:
        return []


def create_wordcloud(st: streamlit, posts):
    wordcloud = WordCloud(background_color="white", max_words=40).generate(
        " ".join([item.get("title") for item in posts])
    )
    fig, _ = plt.subplots()
    plt.imshow(wordcloud)
    plt.axis("off")
    return fig


def render_result(st: streamlit, subreddit: str, header: str, post_type: str):
    if subreddit:
        posts = get_posts(subreddit, post_type=post_type)
        if posts:
            st.header(f"{header}: {process_subreddit_name(subreddit)}")
            wordcloud = create_wordcloud(st, posts)
            st.pyplot(wordcloud)
        else:
            st.error("Invalid subreddit", icon="⚠️")
