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
    console.log("COOK",data)
    const likesCountElement = document.querySelector("span[name='like_count']")
    const likesCount = await getLikeCount(tweet_id)
    console.log(likesCount)
    console.log(likesCountElement.innerHTML)
    likesCountElement.innerHTML = parseTwitterNumber(likesCount)
    const likeElement = element.querySelector("div[name='liked_tweet']")
    console.log("likeElement:", likeElement)
    console.log(likesCountElement.innerHTML)
}

async function getLikeCount(tweet_id) {
    try {
        const response = await fetch(`/${tweet_id}/likes`);
        const clonedResponse = response.clone();

        const data = await clonedResponse.json();

        if (clonedResponse.ok) {
            return data.likes;
        } else {
            throw new Error("Error fetching likes count: Invalid response");
        }
    } catch (error) {
        console.error("Error fetching likes count:", error);
        return 0;
    }
}