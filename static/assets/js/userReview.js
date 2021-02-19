
const userReviewContainer = document.getElementById('user-reviews')


const commentTextBox = document.getElementById('comments')

const onSubmitComment = () => {
    let comment = commentTextBox.value
    let userReviewContainerContent = userReviewContainer.innerHTML

    userReviewContainer.innerHTML= `${userReviewContainerContent}<span><p>${comment}</p></span>`
}