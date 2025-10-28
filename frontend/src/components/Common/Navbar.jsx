import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  Box,
} from '@mui/material';
import InventoryIcon from '@mui/icons-material/Inventory';

export default function Navbar() {
  return (
    <AppBar position="static">
      <Toolbar>
        <InventoryIcon sx={{ mr: 2 }} />
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          StockSmart
        </Typography>
        <Box>
          <Button color="inherit" component={RouterLink} to="/">
            Dashboard
          </Button>
          <Button color="inherit" component={RouterLink} to="/products">
            Products
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
}