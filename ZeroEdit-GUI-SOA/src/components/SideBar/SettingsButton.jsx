//Import the React Framework
import React from "react";

// Importing CSS and Bootstrap
import { Row, Col, Button } from 'react-bootstrap';

const SettingsButton = ({handleClick}) => {
    return (
        <Row style={{height:"4vh"}}>
            <Col >
                <Button 
                    type="button" 
                    className="btn btn-secondary w-100 pt-0"
                    style={{
                        display:"flex",
                        height: "30px", 
                        alignItems:"center", 
                        justifyContent:"start",
                        textAlign:"start"
                    }}
                    onClick={handleClick}
                >
                    <i className="bi bi-gear"></i> &nbsp;
                    Settings
                </Button>
            </Col>
        </Row>
    );
}

export default SettingsButton;