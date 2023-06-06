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
    const likedElement = element.querySelector("div[name='liked_tweet']")
    const notLikedElement = element.querySelector("div[name='not_liked_tweet']")
    console.log("likedElement:", likedElement)
    console.log("notLikedElement:", notLikedElement)
    if (likedElement) {
        likedElement.classList.remove("text-twitter-red")
        likedElement.classList.add("text-twitter-grey")
        likedElement.name = "not_liked_tweet"
    } else {
        notLikedElement.classList.remove("text-twitter-grey")
        notLikedElement.classList.add("text-twitter-red")
        notLikedElement.name = "liked_tweet"
    }
    console.log("likedElement:", likedElement)
    console.log("notLikedElement:", notLikedElement)
    console.log(likesCountElement.innerHTML)
}

async function getLikeCount(tweet_id) {
    try {
        const response = await fetch(`/${tweet_id}/likes`);
        const clonedResponse = response.clone();

        const data = await clonedResponse.json();

        if (clonedResponse.ok) {
            console.log(data.likes, data)
            return data.likes;
        } else {
            throw new Error("Error fetching likes count: Invalid response");
        }
    } catch (error) {
        console.error("Error fetching likes count:", error);
        return 0;
    }
}