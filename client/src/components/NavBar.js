import {NavLink} from "react-router-dom"

function NavBar(){
    return (
        <nav>
            <div>
                <NavLink to="/">Home</NavLink>
            </div>
            <div>
                <NavLink to="/add_hotel">Add Hotel</NavLink>
                <NavLink to="/update_hotel">Update Hotel</NavLink>
            </div>
        </nav>
    )
}

export default NavBar;