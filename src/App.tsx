import React, { useState } from 'react'
import {
  BrowserRouter as Router,
  Route,
  NavLink,
  Link,
} from 'react-router-dom'
import images from './images.jpg'


import '@trussworks/react-uswds/lib/uswds.css'
import '@trussworks/react-uswds/lib/index.css'
import {
  GovBanner,
  Header,
  Title,
  NavMenuButton,
  PrimaryNav,
  GridContainer,
} from '@trussworks/react-uswds'

import HomePage from './pages/Home'
import ExamplePage from './pages/Example'
import FormsPage from './pages/Forms'
import IconsPage from './pages/Icons'
import { Routes } from './routes'

import './App.css'

const App = () => {
  const [mobileNavOpen, setMobileNavOpen] = useState(false)
  const { HOME_PAGE, EXAMPLES_PAGE, FORMS_PAGE, ICONS_PAGE } = Routes
  const BASE_URL = "/api/v1/DPP_agency"

  const toggleMobileNav = (): void => {
    setMobileNavOpen((prevOpen) => !prevOpen)
  }

  const navItems = [
    <NavLink to="/HOME_PAGE" >
      Home
    </NavLink>,
    <NavLink to="/EXAMPLES_PAGE">
      Examples
    </NavLink>,
    <NavLink to="/ICONS_PAGE">
      Icons
    </NavLink>,
  ]

  /*
    function sendUserDataToServer(userID, firstName, user_email) {
      const url = BASE_URL + "/userInfo";
      var data = JSON.stringify({
        "clientId":userID,
        "firstName":firstName,
        "email" : user_email
        
      });
    fetch(url, {
    method: 'POST', // or 'PUT'
    headers: {
      'Content-Type': 'application/json'
    },
    body: data,
  })
  .then(response => {
    console.log(response);
    return response.json();
  })
  .then(data => {
    console.log('Success:', data);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
  }
  */

  return (

    <Router>
      <GovBanner />
      <Header basic>
        <div className="usa-nav-container">
          <div className="usa-navbar">
            <Title>
              <Link to={HOME_PAGE}>Department for the Protection of Pets</Link>
            </Title>
            <NavMenuButton
              label="Menu"
              onClick={toggleMobileNav}
              className="usa-menu-btn"
            />
          </div>

          <PrimaryNav
            aria-label="Primary navigation"
            items={navItems}
            onToggleMobileNav={toggleMobileNav}
            mobileExpanded={mobileNavOpen}
          />
        </div>
        <img src={images} alt="Logo"></img>
        <button> LOGIN</button>
      </Header>




    </Router>

  );
}

export default App