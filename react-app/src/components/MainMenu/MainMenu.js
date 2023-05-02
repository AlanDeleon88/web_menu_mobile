import './MainMenu.css'
import { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useHistory } from 'react-router-dom'
import { getMenus } from '../../store/menus'
import banner from "./assets/HukuBanner.png"
import menuItem from "./assets/sushi.jpeg"
const MainMenu = () =>{

    //! study basic javascript and basic coding. sending commands to the computer.
    //! learn about data types, variables, and functions.
    //! iterating through data and automation

    //* [kitchen, sushibar, drinks]
    const [isLoaded,setIsLoaded] = useState(false)
    const dispatch = useDispatch()
    const history = useHistory()
    const menus = Object.values(useSelector(state=>state.menus))
    /*
        ? [kitchen, sushi bar, drinks, lunch specials]
    */

    useEffect(() =>{
        //! hard coded restaurant_id, figure out a way to dynamically set the id later.
        dispatch(getMenus(1)).then(res =>{
            setIsLoaded(true)
        })

    },[dispatch])


    return(
        <>
            <div className='main-menu-container'>
                <div className='main-menu-header'>
                    <img className='main-menu-banner' src={banner}/>
                </div>
                <div className='main-menu-sub-menu-container'>
                    { isLoaded &&
                        <>
                            {menus.map(el =>{
                                return(
                                    <div className='sub-menu-container' key={el.menu_id} onClick={() =>{
                                        history.push(`/menu/${el.name.replace(/\s/g, '')}/${el.menu_id}`)
                                    }}>
                                        <div className='sub-menu-text-container'>
                                        {el.name}
                                        </div>
                                    </div>
                                )
                            })}

                        </>

                    }

                </div>
            </div>
        </>
    )
}

export default MainMenu
