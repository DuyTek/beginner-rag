import { Theme } from "@emotion/react";
import {
  ComponentsProps,
  ComponentsOverrides,
  ComponentsVariants,
} from "@mui/material";

export const buttonTheme = (): {
  defaultProps?: ComponentsProps["MuiButton"];
  styleOverrides?: ComponentsOverrides<Theme>["MuiButton"];
  variants?: ComponentsVariants["MuiButton"];
} => ({
  styleOverrides: {
    root: {
      padding: "8px 16px",
    },
    sizeSmall: {
      padding: "4px 8px",
    },
    sizeLarge: {
      padding: "12px 24px",
    },
  },
});
