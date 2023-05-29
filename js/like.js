async function like(tweet_id) {
    tweet_id = tweet_id.value
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    console.log("COOK",data)
    const likesCountElement = document.querySelector("input[name='like_count']")
    console.log(likesCountElement, likesCountElement.value)
    const likesCount = await getLikeCount()
    console.log(likesCountElement.innerHTML)
    likesCountElement.innerHTML = likesCount
    console.log(likesCountElement.innerHTML)
}

async function getLikeCount() {
    try {
        const tweet_id = document.querySelector("input[name='tweet_id_likes']").value
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