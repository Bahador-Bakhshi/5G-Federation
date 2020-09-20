graph [
  node [
    id 0
    label 1
    disk 4
    cpu 3
    memory 5
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 3
    memory 11
  ]
  node [
    id 2
    label 3
    disk 3
    cpu 1
    memory 9
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 4
    memory 10
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 6
  ]
  node [
    id 5
    label 6
    disk 10
    cpu 4
    memory 3
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 33
    bw 57
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 192
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 166
  ]
  edge [
    source 0
    target 3
    delay 35
    bw 132
  ]
  edge [
    source 1
    target 5
    delay 31
    bw 92
  ]
  edge [
    source 2
    target 4
    delay 26
    bw 104
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 173
  ]
]
