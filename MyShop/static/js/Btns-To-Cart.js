let updateBtns = document.getElementsByClassName('update-cart')
for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let shopProductID = this.dataset.product
        let action = this.dataset.action
         console.log('pro', this.dataset.product)
        console.log('shopProductID:', shopProductID, 'action:', action)
        console.log('User:', user)
        if (user === 'AnonymousUser') {
            console.log('Not Logged in')
        } else {
            UpdateUserOrder(shopProductID, action)
        }

    })
}

function UpdateUserOrder(shopProductID, action) {
    console.log('User is logged in, sending data..')
    let url = '/update_cart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'shopProductID': shopProductID, 'action': action})
    })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data:', data)
            location.reload()
        })


}