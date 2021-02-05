graph [
  node [
    id 0
    label 1
    disk 8
    cpu 3
    memory 3
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 2
    memory 9
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 1
    memory 9
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 9
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 4
    memory 13
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 1
    memory 10
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 29
    bw 81
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 135
  ]
  edge [
    source 0
    target 2
    delay 27
    bw 173
  ]
  edge [
    source 0
    target 3
    delay 28
    bw 180
  ]
  edge [
    source 1
    target 4
    delay 25
    bw 179
  ]
  edge [
    source 2
    target 4
    delay 27
    bw 138
  ]
  edge [
    source 3
    target 4
    delay 35
    bw 132
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 90
  ]
]
