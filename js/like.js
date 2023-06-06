async function like(element) {
    const user_id = element.querySelector("input[name='user_id']").value
    const tweet_id = element.querySelector("input[name='tweet_id_likes']").value
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    
    const likesElement = document.querySelector(".likes-tweet-id-" + tweet_id)
    likesElement.classList.remove("not-liked-tweet")
    likesElement.classList.add("liked-tweet")
    likesElement.onclick = function() {
        unlike(element)
    }
    console.log("LIKE CLASSLIST", likesElement.classList)
    
    const likesCountElement = document.querySelector(".like-count-" + tweet_id)
    likesCountElement.classList.remove("liked-tweet")
    likesCountElement.classList.add("not-liked-tweet")
    const likesCount = await getLikeCount(tweet_id)
    likesCountElement.innerHTML = parseTwitterNumber(likesCount)
    console.log("LIKE COUNT CLASSLIST", likesCountElement.classList)
}

async function unlike(element) {
    const user_id = element.querySelector("input[name='user_id']").value
    const tweet_id = element.querySelector("input[name='tweet_id_likes']").value
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    
    const likesElement = document.querySelector(".likes-tweet-id-" + tweet_id)
    likesElement.classList.remove("liked-tweet")
    likesElement.classList.add("not-liked-tweet")
    likesElement.onclick = function() {
        like(element)
    }
    console.log("UNLIKE CLASSLIST", likesElement.classList)
    
    const likesCountElement = document.querySelector(".like-count-" + tweet_id)
    likesCountElement.classList.remove("not-liked-tweet")
    likesCountElement.classList.add("liked-tweet")
    const likesCount = await getLikeCount(tweet_id)
    likesCountElement.innerHTML = parseTwitterNumber(likesCount)
    console.log("UNLIKE COUNT CLASSLIST", likesCountElement.classList)
}

async function getLikeCount(tweet_id) {
    try {
        const response = await fetch(`/${tweet_id}/likes`)
        const clonedResponse = response.clone()

        const data = await clonedResponse.json()

        if (clonedResponse.ok) {
            console.log("DATA.LIKES:", data.likes, data)
            return data.likes
        } else {
            throw new Error("Error fetching likes count: Invalid response")
        }
    } catch (error) {
        console.error("Error fetching likes count:", error)
        return 0
    }
}