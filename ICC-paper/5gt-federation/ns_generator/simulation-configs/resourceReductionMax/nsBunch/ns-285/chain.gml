graph [
  node [
    id 0
    label 1
    disk 4
    cpu 2
    memory 7
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 2
    memory 10
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 4
    memory 16
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 6
    cpu 1
    memory 12
  ]
  node [
    id 5
    label 6
    disk 4
    cpu 4
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 25
    bw 54
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 121
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 133
  ]
  edge [
    source 0
    target 3
    delay 32
    bw 107
  ]
  edge [
    source 1
    target 5
    delay 26
    bw 57
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 123
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 156
  ]
  edge [
    source 4
    target 5
    delay 33
    bw 70
  ]
]
