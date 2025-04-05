import {
  Button,
  Checkbox,
  Divider,
  FormControl,
  FormControlLabel,
  Grid,
  InputLabel,
  Paper,
  Stack,
  TextField,
  Typography,
} from "@mui/material";

export const TestScenarioCreationPage = () => {
  return (
    <Stack>
      <Typography variant="h1">Create Test Scenario</Typography>
      <Typography variant="subtitle1">
        Enter details about the test you want to create
      </Typography>
      <Divider sx={{ my: 3 }} />
      <Paper elevation={3} sx={{ height: "100%", padding: 4 }}>
        <form>
          <Grid container spacing={4} columns={12}>
            <Grid container rowSpacing={4} size={6}>
              <TextField label="Website URL" required fullWidth />
              <TextField label="Test Objective" required fullWidth />
              <TextField label="Description" multiline minRows={3} fullWidth />
            </Grid>
            <Grid container rowSpacing={4} size="grow">
              <TextField label="Precondition" multiline minRows={3} fullWidth />
              <Grid>
                <InputLabel>Execution Configurations</InputLabel>
                <FormControl>
                  <FormControlLabel
                    label="Capture Screenshots"
                    control={<Checkbox />}
                  />
                </FormControl>
              </Grid>
            </Grid>
          </Grid>
          <Grid flexDirection="row-reverse" container mt={2}>
            <Button type="submit" variant="contained">
              Submit
            </Button>
          </Grid>
        </form>
      </Paper>
    </Stack>
  );
};
