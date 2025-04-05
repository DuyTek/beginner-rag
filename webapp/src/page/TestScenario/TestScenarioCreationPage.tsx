import { Divider, Paper, Stack, Typography } from "@mui/material";
import { CreateScenarioForm } from "./CreateScenarioForm";

export const TestScenarioCreationPage = () => {
  return (
    <Stack>
      <Typography variant="h1">Create Test Scenario</Typography>
      <Typography variant="subtitle1">
        Enter details about the test you want to create
      </Typography>
      <Divider sx={{ my: 3 }} />
      <Paper elevation={3} sx={{ height: "100%", padding: 4 }}>
        <CreateScenarioForm />
      </Paper>
    </Stack>
  );
};
