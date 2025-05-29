// 비동기 제어

// const user = {}

// setTimeout(() => {
//     user.name = "weniv"
// }, 0)

// console.log(user)


// 콜백함수

const user = {}

// function setUser(callback) {
//     setTimeout(() => {
//         user.name = "weniv"
//         callback(user)
//     }, 0)
// }


// function printUser(user) {
//     console.log(user)
// }

// // setUser(printUser)
// // setUser((user) => console.log(user) )

// function setUser(callback) {
//     setTimeout(() => {
//         user.name = 'weniv'
//         user.age = 20
//         callback(user)
//     })
// }

// function roleCheck(user, callback) {
//     setTimeout(() => {
//         if (user.age >= 20) {
//             user.role = "성인"
//         }
//         else {
//             user.role = "학생"
//         }
//         callback(user)
//     }, 1000)
// }

// setUser((user) => roleCheck(user, printUser))


function 주문접수(음식명, callback) {
    console.log(`${음식명} 주문이 접수되었습니다.`)
    setTimeout(()=>{
        callback(음식명)
    }, 1000)
}

function 음식준비(음식명, callback) {
    console.log(`${음식명} 준비가 완료되었습니다.`)
    setTimeout(() => {
        callback()
    }, 2000)
}

function 배달시작(주소, callback) {
    console.log(`${주소}로 배달을 시작합니다`)
    setTimeout(() => {
        console.log("배달이 완료되었습니다")
        callback()
    }, 3000)
}

주문접수("피자", (음식명)=>{
    음식준비(음식명, () => {
        배달시작("서울시 강남구", () => {
            console.log("배달 완료!")
        })
    })

})