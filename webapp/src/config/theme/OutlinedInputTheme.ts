import {
  ComponentsProps,
  ComponentsOverrides,
  ComponentsVariants,
  Theme,
  outlinedInputClasses,
} from "@mui/material";

export const outlinedInputTheme = (): {
  defaultProps?: ComponentsProps["MuiOutlinedInput"];
  styleOverrides?: ComponentsOverrides<Theme>["MuiOutlinedInput"];
  variants?: ComponentsVariants["MuiOutlinedInput"];
} => ({
  styleOverrides: {
    root: ({ theme }) => ({
      "&:hover": {
        [`& .${outlinedInputClasses.notchedOutline}`]: {
          borderColor: theme.palette.primary.dark,
        },
      },
    }),
    input: ({ theme }) => ({
      padding: theme.spacing(1.5, 2),
    }),
    notchedOutline: ({ theme }) => ({
      borderColor: theme.palette.primary.light,
      borderWidth: 2,
    }),
  },
});
