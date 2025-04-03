import { createTheme, Theme } from "@mui/material";

export const theme: Theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2', // Blue
      light: '#42a5f5',
      dark: '#1565c0',
    },
    secondary: {
      main: '#9c27b0', // Purple
      light: '#ba68c8',
      dark: '#7b1fa2',
    },
    error: {
      main: '#d32f2f',
    },
    warning: {
      main: '#ed6c02',
    },
    info: {
      main: '#0288d1',
    },
    success: {
      main: '#2e7d32',
    },
    background: {
      default: '#f5f5f5',
      paper: '#ffffff',
    },
  },
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    h1: {
      fontSize: '40px',
      fontWeight: 500,
      lineHeight: '48px',
    },
    h2: {
      fontSize: '32px',
      fontWeight: 500,
      lineHeight: '40px',
    },
    h3: {
      fontSize: '28px',
      fontWeight: 500,
      lineHeight: '36px',
    },
    h4: {
      fontSize: '24px',
      fontWeight: 500,
      lineHeight: '32px',
    },
    h5: {
      fontSize: '20px',
      fontWeight: 500,
      lineHeight: '28px',
    },
    h6: {
      fontSize: '16px',
      fontWeight: 500,
      lineHeight: '24px',
    },
    body1: {
      fontSize: '16px',
      lineHeight: '24px',
    },
    body2: {
      fontSize: '14px',
      lineHeight: '20px',
    },
    button: {
      fontSize: '14px',
      textTransform: 'none',
    },
  },
  shape: {
    borderRadius: 4,
  },
  spacing: 4, // Base spacing unit in px
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          padding: '8px 16px',
        },
        sizeSmall: {
          padding: '4px 8px',
        },
        sizeLarge: {
          padding: '12px 24px',
        },
      },
    },
    MuiPaper: {
      styleOverrides: {
        root: {
          padding: '16px',
        },
      },
    },
  },
});