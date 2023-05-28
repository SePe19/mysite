async function like(tweet_id) {
    tweet_id = tweet_id.value
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    const likesCountElement = document.getElementById("likeCount")
    const likesCount = await getLikeCount()
    likesCountElement.textContent = likesCount
}

async function getLikeCount() {
    try {
        const tweet_id = document.getElementById("tweet_id_likes").value
        console.log("YUUYYUUYUYUYUY",tweet_id)
        console.log("YUUYYUUYUYUYUY",tweet_id)
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