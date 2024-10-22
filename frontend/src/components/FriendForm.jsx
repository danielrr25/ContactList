// src/components/FriendForm.jsx
import { 
  Box, 
  Button, 
  FormControl, 
  FormLabel, 
  Input, 
  Modal, 
  ModalBody, 
  ModalCloseButton, 
  ModalContent, 
  ModalFooter, 
  ModalHeader, 
  useToast 
} from '@chakra-ui/react';
import { useState } from 'react';
import axios from 'axios';  // You'll need to install axios

const FriendForm = ({ isOpen, onClose }) => {
  const [name, setName] = useState('');
  const [role, setRole] = useState('');
  const [description, setDescription] = useState('');
  const [gender, setGender] = useState('male');
  const toast = useToast();

  const handleSubmit = async () => {
    try {
      // await axios.post('http://localhost:5000/api/friends', {
        // await axios.post('${BASE_URL}/friends', {
        await axios.post(`${BASE_URL}/friends`, {
        name,
        role,
        description,
        gender
      });
      toast({
        title: "Friend added.",
        description: "Your new friend has been added successfully.",
        status: "success",
        duration: 5000,
        isClosable: true,
      });
      onClose(); // Close the modal on success
    } catch (error) {
      toast({
        title: "An error occurred.",
        description: "Unable to add friend.",
        status: "error",
        duration: 5000,
        isClosable: true,
      });
    }
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <ModalContent>
        <ModalHeader>Add New Friend</ModalHeader>
        <ModalCloseButton />
        <ModalBody>
          <FormControl isRequired>
            <FormLabel>Name</FormLabel>
            <Input 
              value={name} 
              onChange={(e) => setName(e.target.value)} 
            />
          </FormControl>
          <FormControl isRequired mt={4}>
            <FormLabel>Role</FormLabel>
            <Input 
              value={role} 
              onChange={(e) => setRole(e.target.value)} 
            />
          </FormControl>
          <FormControl isRequired mt={4}>
            <FormLabel>Description</FormLabel>
            <Input 
              value={description} 
              onChange={(e) => setDescription(e.target.value)} 
            />
          </FormControl>
          <FormControl isRequired mt={4}>
            <FormLabel>Gender</FormLabel>
            <Input 
              value={gender} 
              onChange={(e) => setGender(e.target.value)} 
            />
          </FormControl>
        </ModalBody>
        <ModalFooter>
          <Button colorScheme="blue" mr={3} onClick={handleSubmit}>
            Save
          </Button>
          <Button variant="outline" onClick={onClose}>
            Cancel
          </Button>
        </ModalFooter>
      </ModalContent>
    </Modal>
  );
};

export default FriendForm;
