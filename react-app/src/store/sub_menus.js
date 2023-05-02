const SET_SUB_MENUS = 'sub_menus/SET_SUB_MENUS'


const setSubMenus = payload =>{
    return {
        type: SET_SUB_MENUS,
        payload
    }
}

export const getSubMenus = menuId => async (dispatch) =>{
    const response = await fetch(`/api/menus/${menuId}`)
    if(response.ok){
        const data = await response.json()
        dispatch(setSubMenus(data.sub_menus))
        return null
    }
}

export default function subMenuReducer(state = {}, action){
    let newState;
    switch(action.type){
        case SET_SUB_MENUS:
            newState={}
            action.payload.forEach(el =>{
                newState[el.id] = el
            })
            return newState;

        default:
            return state
    }
}
