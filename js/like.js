async function like(element) {
    console.log("ELEMENT", element);
    console.log("ELEMENT type", typeof element);
    console.log("ELEMENT instanceof Element", element instanceof Element);
    console.log("ELEMENT instanceof HTMLElement", element instanceof HTMLElement);
    let tweet_id = element.querySelector("input[name='tweet_id_likes']").value
    console.log("VALUE", tweet_id)
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    const likesCountElement = document.querySelector(".like-count-" + tweet_id)
    const likesCount = await getLikeCount(tweet_id)
    likesCountElement.innerHTML = parseTwitterNumber(likesCount)
    const likeButtons = document.getElementsByClassName("likes")
    const likedTweet = document.querySelector(".liked-tweet")
    for (let i = 0; i < likeButtons.length; i++) {
        likeButtons[i].onclick = function() {
            console.log("THIS", element)
            like(element)
        }
        if (likeButtons[i].querySelector(".liked-tweet").value) {
            unlike(element)
            likedTweet.classList.remove("liked-tweet")
            likedTweet.classList.add("not-liked-tweet")
        }
    }
}

async function unlike(element) {
    console.log("ELEMENT", element);
    console.log("ELEMENT type", typeof element);
    console.log("ELEMENT instanceof Element", element instanceof Element);
    console.log("ELEMENT instanceof HTMLElement", element instanceof HTMLElement);
    let tweet_id = element.querySelector("input[name='tweet_id_likes']").value
    console.log("VALUE", tweet_id)
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    const likesCountElement = document.querySelector(".like-count-" + tweet_id)
    const likesCount = await getLikeCount(tweet_id)
    likesCountElement.innerHTML = parseTwitterNumber(likesCount)
    const likeButtons = document.getElementsByClassName("likes")
    const notLikedTweet = document.querySelector(".not-liked-tweet")
    for (let i = 0; i < likeButtons.length; i++) {
        likeButtons[i].onclick = function() {
            console.log("THIS", element)
            like(element)
        }
        if (!likeButtons[i].querySelector(".liked-tweet").value) {
            like(element)
            notLikedTweet.classList.remove("not-liked-tweet")
            notLikedTweet.classList.add("liked-tweet")
        }
    }
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