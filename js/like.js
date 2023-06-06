async function like(element) {
    const user_id = element.querySelector("input[name='user_id']")
    console.log("USER", user_id)
    const tweet_id = element.querySelector("input[name='tweet_id_likes']").value
    console.log("TWEET", tweet_id)
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    console.log(data)
    const likeButtons = document.getElementsByClassName("like")
    for (let i = 0; i < likeButtons.length; i++) {
        if (likeButtons[i].value == user_id) {
            console.log(likeButtons[i].classList)
            likeButtons[i].classList.remove("liked-tweet")
            likeButtons[i].classList.add("not-liked-tweet")
            likeButtons[i].onclick = function() {
                unlike(element)
            }
        }
    }
    console.log(".like-count-" + tweet_id)
    const likesCountElement = document.querySelector(".like-count-" + tweet_id)
    console.log(likesCountElement)
    const likesCount = await getLikeCount(tweet_id)
    likesCountElement.innerHTML = parseTwitterNumber(likesCount)
}

async function unlike(element) {
    let tweet_id = element.getAttribute("value")
    console.log("VALUE", tweet_id)
    const formData = new FormData()
    formData.append('tweet_id', tweet_id)
    const response = await fetch("/like", {
        method: "POST",
        body: formData
    })
    const data = await response.json()
    const likeButtons = document.getElementsByClassName("like")
    for (let i = 0; i < likeButtons.length; i++) {
        if (likeButtons[i].value == tweet_id) {
            console.log(likeButtons[i].classList)
            likeButtons[i].classList.remove("not-liked-tweet")
            likeButtons[i].classList.add("liked-tweet")
            likeButtons[i].onclick = function() {
                like(element)
            }
        }
    }
    const likesCountElement = document.querySelector(".like-count-" + tweet_id)
    const likesCount = await getLikeCount(tweet_id)
    likesCountElement.innerHTML = parseTwitterNumber(likesCount)
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