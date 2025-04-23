import React, { useState } from 'react';
import { Modal, Button, Form } from 'react-bootstrap';

function PermissionsPopup({ show, onHide, modalSize = 'md', selectedUser=""}) {
  // Local state for the permission toggles
  const [readPermission, setReadPermission] = useState(false);
  const [writePermission, setWritePermission] = useState(false);
  const [executePermission, setExecutePermission] = useState(false);

  // Handle save button click
  const handleSave = () => {
    console.log({
      read: readPermission,
      write: writePermission,
      execute: executePermission,
    });
    onHide();
  };

  // Inline style for icons – ensuring green and larger size
  const iconStyle = { color: '#0d6efd', fontSize: '1.5rem' };

  return (
    <Modal show={show} onHide={onHide} centered size={modalSize}>
      <Modal.Header closeButton>
        <Modal.Title className="w-100 text-center">
          <div className="d-flex justify-content-center align-items-center">
            <span className="me-2">Permissions for {selectedUser}</span>
            {/* Header Icon */}
            <i className="bi bi-shield-lock-fill" style={iconStyle} />
          </div>
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        {/* Permission Row for "Read" */}
        <div className="d-flex align-items-center justify-content-between mb-3">
          <div className="d-flex align-items-center">
            {/* Read Icon */}
            <i className="bi bi-eye" style={iconStyle} />
            <span className="ms-2">Read</span>
          </div>
          <Form.Check
            type="switch"
            id="read-switch"
            checked={readPermission}
            onChange={() => setReadPermission(prev => !prev)}
          />
        </div>
        {/* Permission Row for "Write" */}
        <div className="d-flex align-items-center justify-content-between mb-3">
          <div className="d-flex align-items-center">
            {/* Write Icon */}
            <i className="bi bi-pencil" style={iconStyle} />
            <span className="ms-2">Write</span>
          </div>
          <Form.Check
            type="switch"
            id="write-switch"
            checked={writePermission}
            onChange={() => setWritePermission(prev => !prev)}
          />
        </div>
        {/* Permission Row for "Execute" */}
        <div className="d-flex align-items-center justify-content-between">
          <div className="d-flex align-items-center">
            {/* Execute Icon */}
            <i className="bi bi-gear" style={iconStyle} />
            <span className="ms-2">Execute</span>
          </div>
          <Form.Check
            type="switch"
            id="execute-switch"
            checked={executePermission}
            onChange={() => setExecutePermission(prev => !prev)}
          />
        </div>
      </Modal.Body>
      <Modal.Footer className="d-flex justify-content-center">
        <Button variant="success" onClick={handleSave}>
          {/* Save Icon */}
         
          Save 
        </Button>
      </Modal.Footer>
    </Modal>
  );
}

export default PermissionsPopup;
