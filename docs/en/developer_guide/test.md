# Test Guide

## CPU-Friendly Unit Tests

Use the CPU-friendly UT entrypoint first when you want coverage output and test artifacts without relying on the full NPU runtime stack.

```bash
python -m pip install -r requirements.txt
python -m pip install -r requirements-test.txt
bash tests/run_UT_test.sh
```

Artifacts are generated under `tests/UT/`, including:

- `run_UT.log`
- `final.xml`
- `coverage.xml`
- `htmlcov/`

The repository also provides `tests/scripts/check_coverage.py` for CI coverage gating on newly added Python files.

## Full Test Entry

When the Ascend/NPU runtime stack is available, run the wrapper script for the full test entry:

```bash
bash tests/run_test.sh --all
```

Available options:

- `--cpu_only`
- `--npu_only`
- `--all`

## LA Operator Accuracy Test

This section describes how to run LA operator accuracy verification in the MindIE SD repository.

1. If needed, uninstall the currently installed MindIE SD package first:

   ```bash
   pip uninstall mindiesd
   ```

2. Update `tests/plugin/la_acc_prof.py`, choose Option 1 or Option 2, and load either `test_la.csv` or `enumerated_cases.csv` to verify LA accuracy under the required shapes.

   - `./tests/plugin/test_la.csv`: common input shapes used by SD models
   - `enumerated_cases.csv`: enumerated shape combinations

3. Run the script:

   ```bash
   cd tests
   python plugin/la_acc_prof.py
   ```

After the run, result files are generated in the repository root and can be used to inspect similarity between LA and FAScore outputs.

## Common Exceptions

When using MindIE SD for inference, users are responsible for the safety of model files such as weights, configuration files, and model code. Common exceptions include:

- If default model configuration values are changed during initialization, interfaces may be affected; excessively large weights or configuration values may trigger out-of-memory errors such as `RuntimeError: NPU out of memory. Tried to allocate xxx GiB.`.
- Large tensor shapes during inference may also trigger similar out-of-memory errors.
- Invalid input or environment mismatch may raise exceptions that should be handled by upper-layer services.

| Exception Type | Description |
| -- | -- |
| ZeroDivisionError | Division by zero. |
| ValueError | Invalid parameter value. |
