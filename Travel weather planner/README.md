# Commute Decision

A tiny, dependency-free Python tool that decides **whether you should travel right now**, based on distance, weather, and what transportation options you have available.

## How it works

The decision is based on five inputs:

| Input | Type | Description |
|---|---|---|
| `distance_mi` | `float` | Distance to your destination, in miles |
| `is_raining` | `bool` | Whether it's currently raining |
| `has_bike` | `bool` | Whether you have a bike available |
| `has_car` | `bool` | Whether you have a car available |
| `has_ride_share_app` | `bool` | Whether you have a ride-share app (Uber, Lyft, etc.) available |

### Decision rules

1. **No distance** (`distance_mi == 0`) → not recommended.
2. **Short trip** (`distance_mi <= 1`):
   - Not raining → walk (recommended)
   - Raining → not recommended
3. **Medium trip** (`1 < distance_mi <= 6`):
   - No bike → not recommended
   - Bike available, not raining → bike (recommended)
   - Bike available, raining → not recommended (avoid biking in the rain)
4. **Long trip** (`distance_mi > 6`):
   - Ride-share app or car available → recommended
   - Neither available → not recommended

## Usage

```bash
python commute_decision.py
```

Or import it directly in your own code:

```python
from commute_decision import CommuteConditions, should_travel

conditions = CommuteConditions(
    distance_mi=4,
    is_raining=True,
    has_bike=True,
    has_car=True,
    has_ride_share_app=True,
)

print(should_travel(conditions))  # False
```

## Running tests

This project uses Python's built-in `unittest` framework. No external dependencies are required.

```bash
python -m unittest test_commute_decision.py -v
```

## Project structure

```
.
├── commute_decision.py        # Core decision logic
├── test_commute_decision.py   # Unit tests
├── requirements.txt           # Dependencies (none — standard library only)
├── LICENSE
└── README.md
```

## Requirements

- Python 3.7+
- No external packages required

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
