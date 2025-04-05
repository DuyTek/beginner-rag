import {
  Button,
  Checkbox,
  FormControl,
  FormControlLabel,
  Grid,
  TextField,
} from "@mui/material";
import { SubInputLabel } from "../../components";

export const CreateScenarioForm = () => {
  return (
    <form>
      <Grid container spacing={4} columns={12}>
        <Grid container rowSpacing={4} size={4}>
          <TextField label="Website URL" required fullWidth />
          <TextField label="Test Objective" required fullWidth />
          <TextField label="Description" multiline minRows={3} fullWidth />
          <TextField label="Precondition" multiline minRows={3} fullWidth />
        </Grid>
        <Grid container rowSpacing={4} size="grow">
          <Grid>
            <SubInputLabel>Execution Configurations</SubInputLabel>
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
  );
};
