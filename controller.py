import numpy as np
from typing import List, Tuple

class Controller:
    def __init__(self, physics_engine, target_trajectory: List[Tuple[float, np.ndarray]]):
        """
        Initialize the Controller.

        Parameters:
        - physics_engine: The physics engine object.
        - target_trajectory: A list of tuples containing (time, target_state) pairs.
        """
        self.physics_engine = physics_engine
        self.target_trajectory = target_trajectory
        self.current_time = 0.0
        self.current_index = 0

        # Check for invalid target trajectories
        if not target_trajectory:
            raise ValueError("Target trajectory is empty")

        # Pre-process target trajectory for interpolation
        self.interpolated_trajectory = self.interpolate_trajectory(target_trajectory)

    def control_loop(self, dt: float):
        """
        Main control loop of the simulation.

        Parameters:
        - dt: Time step for the simulation.
        """
        while not self.check_termination_conditions():
            self.update_control_inputs()
            self.physics_engine.simulate_step(dt)
            self.current_time += dt

    def update_control_inputs(self):
        """
        Update control inputs based on interpolated target trajectory.
        """
        # Get interpolated target state at current time
        target_state = self.get_interpolated_target_state()
        # Calculate control input (placeholder for now)
        control_input = self.calculate_control_input(target_state)
        # Apply control input to physics engine
        self.physics_engine.apply_control_input(control_input)

    def get_interpolated_target_state(self):
        """
        Get interpolated target state at current time.

        Returns:
        - Interpolated target state.
        """
        # Find nearest index in interpolated trajectory
        idx = np.searchsorted(self.interpolated_trajectory[:, 0], self.current_time)
        # Get nearest time points for interpolation
        t1, t2 = self.interpolated_trajectory[max(0, idx - 1): idx + 1, 0]
        # Perform linear interpolation between target states
        target_state_1, target_state_2 = self.interpolated_trajectory[max(0, idx - 1): idx + 1, 1]
        interp_fraction = (self.current_time - t1) / (t2 - t1)
        interpolated_target_state = target_state_1 + interp_fraction * (target_state_2 - target_state_1)
        return interpolated_target_state

    def calculate_control_input(self, target_state: np.ndarray):
        """
        Calculate control input based on the target state.

        Placeholder method. Needs to be implemented for specific control algorithm.
        """
        # Placeholder: Return zero array as control input
        return np.zeros_like(target_state)

    def check_termination_conditions(self):
        """
        Check termination conditions for the simulation.

        Returns:
        - Boolean indicating whether the simulation should terminate.
        """
        # Check if end of target trajectory is reached
        if self.current_time >= self.target_trajectory[-1][0]:
            return True
        # Additional termination conditions (e.g., specific state, time limit) can be added here
        return False

    @staticmethod
    def interpolate_trajectory(target_trajectory: List[Tuple[float, np.ndarray]]):
        """
        Interpolate target trajectory for smoother control transitions.

        Parameters:
        - target_trajectory: Original target trajectory.

        Returns:
        - Interpolated target trajectory.
        """
        # Convert target_trajectory to numpy array for easier manipulation
        target_trajectory = np.array(target_trajectory)
        # Perform linear interpolation between target states
        interpolated_trajectory = np.vstack(
            [np.linspace(t1, t2, max(int((t2 - t1) / 0.1), 2)), 
             np.array([np.interp(np.linspace(t1, t2, max(int((t2 - t1) / 0.1), 2)), 
                                [t1, t2], [state1, state2]) for t1, t2, state1, state2 in 
                                zip(target_trajectory[:-1, 0], target_trajectory[1:, 0], 
                                    target_trajectory[:-1, 1], target_trajectory[1:, 1])])]
        return interpolated_trajectory.T

# Example usage:
if __name__ == "__main__":
    # Initialize physics engine and target trajectory
    physics_engine = PhysicsEngine()
    target_trajectory = [(0.0, np.array([0, 0])), (1.0, np.array([1, 1])), (2.0, np.array([2, 2]))]

    # Create controller instance and simulate
    controller = Controller(physics_engine, target_trajectory)
    controller.control_loop(dt=0.1)
