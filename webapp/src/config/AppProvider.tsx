import React from "react";
import { CssBaseline, ThemeProvider } from "@mui/material";
import { theme } from "./theme";

export const AppProviders = ({ children }: { children: React.ReactNode }) => {
    let node = children;


    node = <ThemeProvider theme={theme}>{node}</ThemeProvider>
    node = <CssBaseline>{node}</CssBaseline>
    
    return (
        <ThemeProvider theme={theme}>
            <CssBaseline />
            {children}
        </ThemeProvider>
    )
}