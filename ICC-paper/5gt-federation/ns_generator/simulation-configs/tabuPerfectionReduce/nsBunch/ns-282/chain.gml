graph [
  node [
    id 0
    label 1
    disk 7
    cpu 2
    memory 10
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 4
    memory 2
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 1
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 3
    memory 2
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 27
    bw 193
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 146
  ]
  edge [
    source 1
    target 2
    delay 35
    bw 74
  ]
  edge [
    source 1
    target 3
    delay 27
    bw 59
  ]
  edge [
    source 2
    target 4
    delay 32
    bw 61
  ]
  edge [
    source 3
    target 4
    delay 33
    bw 98
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 154
  ]
]
