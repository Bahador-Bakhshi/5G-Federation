graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 5
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 14
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 4
    memory 10
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 14
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 3
    memory 12
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 3
    memory 2
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 35
    bw 163
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 137
  ]
  edge [
    source 0
    target 2
    delay 28
    bw 74
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 54
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 192
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 72
  ]
  edge [
    source 4
    target 5
    delay 26
    bw 98
  ]
]
