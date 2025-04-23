import React from 'react';
import { Modal, Button } from 'react-bootstrap';

const ConfirmModal = ({
  show,
  onClose,
  onConfirm,
  title = "Are you sure?",
  message = "This action cannot be undone.",
  confirmText = "Confirm",
  cancelText = "Cancel",
  confirmVariant = "primary",
  cancelVariant = "secondary",
}) => (
  <Modal show={show} onHide={onClose} centered>
    <Modal.Header closeButton>
      <Modal.Title>{title}</Modal.Title>
    </Modal.Header>
    <Modal.Body>{message}</Modal.Body>
    <Modal.Footer>
      <Button variant={cancelVariant} onClick={onClose}>
        {cancelText}
      </Button>
      <Button variant={confirmVariant} onClick={() => {
        onConfirm?.(); // If defined, run it
        onClose();     // Then close modal
      }}>
        {confirmText}
      </Button>
    </Modal.Footer>
  </Modal>
);

export default ConfirmModal;
