import { Header } from "./Header";
import { Footer } from "./Footer";
import { Box } from "@mui/material";

export function AppLayout({ children }: { children: React.ReactNode }) {
  return (
    <Box
      sx={{
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh",
      }}
    >
      <Header />
      <Box component="main" sx={{ flexGrow: 1, py: 2, px: 2 }}>
        {children}
      </Box>
      <Footer />
    </Box>
  );
}
