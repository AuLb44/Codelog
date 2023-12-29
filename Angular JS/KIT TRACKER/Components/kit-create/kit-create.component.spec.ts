import { ComponentFixture, TestBed } from '@angular/core/testing';
import { KitCreateComponent } from './kit-create.component';

describe('KitCreateComponent', () => {
  let component: KitCreateComponent;
  let fixture: ComponentFixture<KitCreateComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [KitCreateComponent]
    });
    fixture = TestBed.createComponent(KitCreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
