import { useState, useEffect } from "react"
import { useDispatch,useSelector } from "react-redux"
import { useParams } from "react-router-dom"
import { getSubMenus } from "../../store/sub_menus"
import './Menu.css'

const Menu = () =>{
    const dispatch = useDispatch()
    const { name , menuId} = useParams()
    const [isLoaded, setIsLoaded] = useState(false)
    const subMenus = Object.values(useSelector(state=>state.subMenus))
    //! dispatch to get a menu's sub menu.

    useEffect(() =>{
        dispatch(getSubMenus(menuId)).then(res =>{
            setIsLoaded(true)
        })
    }, [dispatch])

    return(
        <>
            <div className="menu-main-container">
                <div>
                    header
                </div>
                <div className="menu-sub-menu-buttons-container">
                {
                    subMenus.map(el =>{
                        return(
                                <div className="sub-menu-buttons">{el.name} </div>
                                )
                            })
                }
                </div>
            </div>
        </>
    )
}

export default Menu
