graph [
  node [
    id 0
    label 1
    disk 7
    cpu 1
    memory 8
  ]
  node [
    id 1
    label 2
    disk 9
    cpu 3
    memory 15
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 3
    memory 3
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 2
    memory 3
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 3
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 32
    bw 199
  ]
  edge [
    source 0
    target 1
    delay 33
    bw 143
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 67
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 61
  ]
  edge [
    source 2
    target 3
    delay 29
    bw 121
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 165
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 59
  ]
]
