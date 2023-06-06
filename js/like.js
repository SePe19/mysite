async function like(element) {
    let tweet_id = element.querySelector("input[name='tweet_id_likes']").value;
    console.log(tweet_id)
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    const likesCountElement = document.querySelector("span[name='like_count']")
    const likesCount = await getLikeCount(tweet_id)
    likesCountElement.innerHTML = parseTwitterNumber(likesCount)
    const likedElement = element.querySelector(".liked-tweet")
    const notLikedElement = element.querySelector(".not-liked-tweet")
    if (likedElement) {
        likedElement.classList.remove("liked-tweet")
        likedElement.classList.add("not-liked-tweet")
    } else {
        notLikedElement.classList.remove("not-liked-tweet")
        notLikedElement.classList.add("liked-tweet")
    }
}

async function getLikeCount(tweet_id) {
    try {
        const response = await fetch(`/${tweet_id}/likes`);
        const clonedResponse = response.clone();

        const data = await clonedResponse.json();

        if (clonedResponse.ok) {
            console.log("DATA.LIKES:", data.likes, data)
            return data.likes;
        } else {
            throw new Error("Error fetching likes count: Invalid response");
        }
    } catch (error) {
        console.error("Error fetching likes count:", error);
        return 0;
    }
}