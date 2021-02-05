graph [
  node [
    id 0
    label 1
    disk 8
    cpu 4
    memory 8
  ]
  node [
    id 1
    label 2
    disk 8
    cpu 3
    memory 15
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 13
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 1
    memory 13
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 3
    memory 5
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 1
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 83
  ]
  edge [
    source 0
    target 1
    delay 27
    bw 68
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 156
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 75
  ]
  edge [
    source 2
    target 3
    delay 30
    bw 168
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 112
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 121
  ]
]
