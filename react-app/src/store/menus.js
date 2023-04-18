
const SET_MENU = 'menus/SET_MENUS'


const setMenu = payload =>{
    return{
        type: SET_MENU,
        payload
    }
}

export const getMenus = restaurantId => async (dispatch) =>{
    console.log(restaurantId);
    const response = await fetch(`/api/restaurants/${restaurantId}/menus`)

    if(response.ok){
        const data = await response.json()
        // console.log(data.menus)
        dispatch(setMenu(data.menus))
        return null
    }
    // else{
    //     const data = await response.json()
    //     return data;
    // }
}

export default function menuReducer(state = {}, action){
    let newState;
    switch(action.type){
        case SET_MENU:
            newState = {}

            action.payload.forEach(menu =>{
                newState[menu.menu_id] = menu
            })
            return newState
        default:
            return state
    }
}
