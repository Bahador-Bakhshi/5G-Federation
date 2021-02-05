graph [
  node [
    id 0
    label 1
    disk 10
    cpu 1
    memory 12
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 1
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 3
    memory 5
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 4
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 1
    memory 4
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 16
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 59
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 164
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 61
  ]
  edge [
    source 1
    target 3
    delay 31
    bw 166
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 95
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 170
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 59
  ]
]
